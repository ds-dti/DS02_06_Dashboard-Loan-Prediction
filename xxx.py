import streamlit as st
import streamlit.components.v1 as stc

# for csv file 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def main():

    menu = ["Home","Eksplorasi", "Prediksi"]

    choice = st.sidebar.selectbox("Menu",menu)

    # HOME
    if choice == "Home":
        st.title("Loan Prediction")
        st.markdown("""
            Aplikasi dapat membantu mengklasifikasikan resiko dalam peminjaman kepada nasabah. Aoakah nasabah mampu untuk membayar pinjaman atau tidak.
            * Pastikan tidak ada data kosong, derau, dan semua data telah siap digunakan sehingga program dapat melakukan prediksi dengan baik.
            * Contoh bentuk data yang dapat Anda gunakan bisa dilihat [di sini](https://github.com/allisonhorst/palmerpenguins)
            * Menu Eksplorasi untuk melakukan eksplorasi terhadap data Anda
            * Menu Prediksi untuk melakukan prediksi terhadap data Anda
        """)
    
    # EKSPLORASI
    elif choice == "Eksplorasi":
        st.title("Eksplorasi")
        st.markdown("""
           Anda dapat melakukan eksplorasi terhadap data Anda
        """)
        st.subheader("Upload Dataset")
        # st.write("Please upload a CSV file format!")
        # df = pd.read_csv(data)
        # upload dataset
        data_file = st.file_uploader("Upload File CSV", type=["csv"])
        if data_file is not None:
        #     df = pd.read_csv(data_file)
            # menampilkan dataset
            df = pd.read_csv(data_file)
            st.dataframe(df)

            st.write("========================================================================")

            st.title("Eksplorasi Data Kategorikal")
            categorical_option = st.selectbox('Choose categorical column:', df.columns)
            # st.write(df[categorical_option].value_counts())
            st.write(df[categorical_option].dtypes)
            if st.button("Lihat"):

                if df[categorical_option].dtypes == 'object':
                    st.write(df[categorical_option].value_counts())

                    # PAIRPLOT
                    st.title("Pairplot")
                    fig = sns.pairplot(df, hue=categorical_option)
                    st.pyplot(fig)

                    # COUNTPLOT
                    st.title("Countplot")
                    st.subheader(categorical_option)
                    fig, ax = plt.subplots()
                    ax = sns.countplot(data=df, x=categorical_option)
                    st.pyplot(fig)

                else:
                    st.write("Kolom yang Anda pilih tidak bertipe Kategorikal")

            st.write("========================================================================")

            st.title("Correlation Map")
            fig, ax = plt.subplots()
            ax = sns.heatmap(df.corr(),cmap='coolwarm',annot=True)
            st.pyplot(fig)

            st.write("========================================================================")

            st.title("Boxplot")
            st.write("""
                Salah satu fitur yang dipilih harus bertipe Kategori atau Numerik
            """)
            selected_fitur = st.multiselect('Pilih 2 Atribut:', df.columns)
            if st.button("Tampilkan Bloxplot"):
                fig, ax = plt.subplots()
                # ax = sns.heatmap(df.corr(),cmap='coolwarm',annot=True)
                ax = sns.boxplot(x=df[selected_fitur[0]],y=df[selected_fitur[1]],data=df,palette='winter')
                st.pyplot(fig)

            # else:
            #     st.write("None")

            st.write("========================================================================")

            st.title("Mean")
            mean_option = st.selectbox('Choose one column:', df.columns)
            if st.button("Tampilkan Mean"):
                if df[mean_option].dtypes == 'object':
                    st.write("""
                        Anda memilih kolom bertipe Kategorikal, 
                        silahkan pilih kolom Numerik
                    """)
                else:
                    st.subheader(df[mean_option].mean())

    # PREDIKSI
    elif choice == "Prediksi":
        st.title("Prediksi-Loan Prediction")
        st.markdown("""
            * Pastikan tidak ada data kosong, derau, dan semua data telah siap digunakan sehingga program dapat melakukan prediksi dengan baik.
            * Contoh bentuk data yang dapat Anda gunakan bisa dilihat [di sini](https://github.com/allisonhorst/palmerpenguins)
        """)
        st.subheader("Upload Dataset")
        st.write("Please upload a CSV file format!")
        # upload dataset
        data_file_prediksi = st.file_uploader("Upload File CSV", type=["csv"])
        if data_file_prediksi is not None:
            df_prediksi = pd.read_csv(data_file_prediksi)
            # menampilkan dataset
            st.dataframe(df_prediksi)

            gender = [0, 1]
            gender_choice = st.selectbox('Jenis Kelamin',gender)
            married = [0, 1]
            married_choice = st.selectbox('Sudah Menikah?',married)
            number = st.number_input('Insert a number')

            X = df_prediksi.drop('Loan_Status', axis=1)
            y = df_prediksi['Loan_Status']

            # # st.write(df[categorical_option].value_counts())
            # st.write(df_prediksi[class_option].dtypes)
            if st.button("Run"):
                st.header("Prediksi")
                st.subheader("hasil:")
            


if __name__ == "__main__":
    main()
