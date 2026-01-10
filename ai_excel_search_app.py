import streamlit as st
import pandas as pd
import os
from openai import OpenAI
from dotenv import load_dotenv

st.set_page_config(page_title="AI Excel Search App", layout="wide")
st.title("🤖 AI-Powered Excel Data Search App")

# -----------------------------
# 1️⃣ Load OpenAI API Key
# -----------------------------
# Priority: Streamlit secrets (cloud) > .env (local)
try:
    API_KEY = st.secrets["OPENAI_API_KEY"]
except Exception:
    load_dotenv()
    API_KEY = os.getenv("OPENAI_API_KEY")

if not API_KEY:
    st.error("❌ OpenAI API key not found. Please set it in .env (local) or Streamlit secrets (cloud).")
    st.stop()

client = OpenAI(api_key=API_KEY)

# -----------------------------
# 2️⃣ File Upload
# -----------------------------
uploaded_files = st.file_uploader(
    "Upload Excel files (daily updates)", 
    type=["xlsx", "xls"], 
    accept_multiple_files=True
)

if uploaded_files:
    df_list = []
    for file in uploaded_files:
        try:
            df_list.append(pd.read_excel(file))
        except Exception as e:
            st.warning(f"Failed to read {file.name}: {e}")

    if df_list:
        data = pd.concat(df_list, ignore_index=True)
        st.success(f"Uploaded {len(uploaded_files)} files — Total rows: {len(data)}")

        # -----------------------------
        # 3️⃣ AI Query
        # -----------------------------
        st.write("### 💬 Ask a question about your data")
        query = st.text_input("Example: 'Show March rows where Amount > 5000'")

        if query:
            st.write("⏳ AI is processing your query…")

            prompt = f"""
            You are a data assistant. The pandas DataFrame is named 'data'.
            Columns: {list(data.columns)}

            User query: {query}

            Write ONLY valid pandas code to filter the DataFrame.
            Assign results to a variable called 'filtered_df'.
            Make it safe to run even if columns contain spaces or special characters.
            """

            try:
                response = client.chat.completions.create(
                    model="gpt-4.1-mini",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0
                )

                code = response.choices[0].message["content"]
                st.code(code, language="python")

                # Execute generated code safely
                local_vars = {"data": data}
                exec(code, {}, local_vars)
                filtered_df = local_vars["filtered_df"]

                st.write("### 🔍 Results")
                st.dataframe(filtered_df)

                if not filtered_df.empty:
                    csv = filtered_df.to_csv(index=False).encode("utf-8")
                    st.download_button(
                        label="⬇️ Download Results",
                        data=csv,
                        file_name="ai_search_results.csv",
                        mime="text/csv"
                    )

            except Exception as e:
                st.error("⚠️ AI failed to generate or execute code.")
                st.error(str(e))
    else:
        st.warning("No valid Excel files uploaded.")
else:
    st.info("Upload today's Excel files to begin.")
