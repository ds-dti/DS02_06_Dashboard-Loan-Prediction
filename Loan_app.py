import streamlit as st
import streamlit.components.v1 as stc

# for csv file
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# for model_selection
import sklearn
from sklearn.model_selection import train_test_split
# import model
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB

# for evaluation
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, precision_score, recall_score, f1_score, roc_curve, roc_auc_score

# Analisis Model Decision Tree


def model_Decision_Tree(selected_model, X_train, X_test, y_train, y_test):
    # st.title(selected_model)
    st.title("Analisis Model Decision Tree")
    dtc = tree.DecisionTreeClassifier(
        min_impurity_decrease=0.001)
    dtc.fit(X_train, y_train)
    y_pred_dtc = dtc.predict(X_test)

    st.subheader("Confusion Matrix Decision Tree")
    st.write(confusion_matrix(y_pred_dtc, y_test))
    st.subheader("Classification Report Decision Tree")
    st.write(classification_report(y_pred_dtc, y_test))
    st.subheader("Akurasi Decision Tree")
    st.write(accuracy_score(y_pred_dtc, y_test))
    y_pred_dtc_proba = dtc.predict_proba(X_test)[::, 1]
    st.subheader("ROC Score Decision Tree")
    aucdtc = roc_auc_score(y_test, y_pred_dtc_proba)
    st.write(aucdtc)

    return dtc

# Analisis Model Random Forest


def model_Random_Forest(selected_model, X_train, X_test, y_train, y_test):
    # st.title(selected_model)
    st.title("Analisis Model Random Forest")
    rf = RandomForestClassifier(n_estimators=250)
    rf.fit(X_train, y_train)
    y_pred_rf = rf.predict(X_test)

    st.subheader("Confusion Matrix Random Forest")
    st.write(confusion_matrix(y_pred_rf, y_test))
    st.subheader("Classification Report Random Forest")
    st.write(classification_report(y_pred_rf, y_test))
    st.subheader("Akurasi Random Forest")
    st.write(accuracy_score(y_pred_rf, y_test))
    y_pred_rf_proba = rf.predict_proba(X_test)[::, 1]
    st.subheader("ROC Score Random Forest")
    aucrf = roc_auc_score(y_test, y_pred_rf_proba)
    st.write(aucrf)

    return rf

# Analisis model Naive Bayes


def model_Naive_Bayes(selected_model, X_train, X_test, y_train, y_test):
    st.title("Analisis Model Naive Bayes")
    # st.title(selected_model)
    gnb = GaussianNB()
    gnb.fit(X_train, y_train)
    y_pred_gnb = gnb.predict(X_test)

    st.subheader("Confusion Matrix Naive Bayes")
    st.write(confusion_matrix(y_pred_gnb, y_test))
    st.subheader("Classification Report Naive Bayes")
    st.write(classification_report(y_pred_gnb, y_test))
    st.subheader("Akurasi Naive Bayes")
    st.write(accuracy_score(y_pred_gnb, y_test))
    y_pred_gnb_proba = gnb.predict_proba(X_test)[::, 1]
    st.subheader("ROC Score Naive Bayes")
    aucgnb = roc_auc_score(y_test, y_pred_gnb_proba)
    st.write(aucgnb)

    return gnb

# Prediksi Data Baru


def prediksi_data_baru(model):
    st.title("Prediksi Data Baru")
    st.subheader("**Pilih Nilai-nilai untuk diprediksi**")
    gender = [0, 1]
    gender_choice = st.selectbox('Gender', gender)
    married = [0, 1]
    married_choice = st.selectbox('Married', married)
    dependent = [0, 1, 2, 3]
    dependent_choice = st.selectbox('Dependent', dependent)
    education = [0, 1]
    education_choice = st.selectbox('Education', education)
    self_employee = [0, 1]
    self_employee_choice = st.selectbox('Self Employee', self_employee)

    applicant_income = st.number_input('Insert Applicant Income')
    coapplicant_income = st.number_input('Inser Coapplicant Income')
    loan_amount = st.number_input('Input Loan Amount')
    loan_amount_term = st.number_input('Input Loan Amount Term')

    credit = [0, 1]
    credit_choice = st.selectbox('Credit History', credit)

    property_area = [0, 1, 2]
    property_area_choice = st.selectbox(
        'Property Area', property_area)

    if st.button("Loan?"):
        st.write(model)
        hasil_prediksi_data_baru = model.predict([[gender_choice, married_choice, dependent_choice, education_choice, self_employee_choice,
                                                   applicant_income, coapplicant_income, loan_amount, loan_amount_term, credit_choice, property_area_choice]])[0]
        st.header(hasil_prediksi_data_baru)


def main():

    # Menu
    menu = ["Beranda", "Eksplorasi", "Uji Model", "Tentang"]
    choice = st.sidebar.selectbox("Menu", menu)

    # Inisialisasi Model
    decision_tree = tree.DecisionTreeClassifier(
        min_impurity_decrease=0.001)
    random_forest = RandomForestClassifier(n_estimators=250)
    naive_bayes = GaussianNB()

    # HOME
    if choice == "Beranda":
        st.markdown('<style>h1{color: red;}</style>', unsafe_allow_html=True)
        st.title("Loan Prediction")
        st.markdown("""
            Aplikasi dapat membantu mengklasifikasikan resiko dalam peminjaman kepada nasabah. Apakah nasabah mampu untuk membayar pinjaman atau tidak berdasarkan atribut-atribut dari dataset. 
            Berikut adalah menu yang ada dalam apkikasi:
            * **Menu Eksplorasi** untuk melakukan eksplorasi terhadap data Anda
            * **Menu Prediksi** untuk melakukan prediksi terhadap data Anda

            **Perhatikan!**
            
            Pastikan tidak ada data kosong, derau, dan semua data telah siap digunakan sehingga program dapat melakukan prediksi dengan baik.
            * Contoh bentuk data yang dapat Anda gunakan bisa dilihat dibawah:
                * Contoh data untuk **Menu Eksplorasi** yang dapat Anda gunakan bisa dilihat [di sini](https://github.com/allisonhorst/palmerpenguins)
                * Contoh data untuk **Menu Prediksi** yang dapat Anda gunakan bisa dilihat [di sini](https://github.com/allisonhorst/palmerpenguins)
        """)

    # EKSPLORASI
    elif choice == "Eksplorasi":
        st.markdown('<style>h1{color: red;}</style>', unsafe_allow_html=True)
        st.title("Eksplorasi")
        st.markdown("""
            Anda dapat melakukan eksplorasi terhadap data Anda
            * Pastikan tidak ada data kosong, derau, dan semua data telah siap digunakan sehingga program dapat melakukan prediksi dengan baik.
            * Contoh bentuk data yang dapat Anda gunakan bisa dilihat [di sini](https://github.com/allisonhorst/palmerpenguins)
        """)

        # upload dataset
        st.subheader("Upload Dataset")
        data_file = st.file_uploader("Upload File CSV", type=["csv"])
        if data_file is not None:

            # menampilkan dataset
            df = pd.read_csv(data_file)
            st.dataframe(df)

            st.write(
                "========================================================================")

            st.subheader("Eksplorasi Data Kategorikal")
            categorical_option = st.selectbox(
                'Choose categorical column:', df.columns)
            st.write(df[categorical_option].dtypes)
            st.write(df[categorical_option].value_counts())

            if st.button("Lihat"):
                if df[categorical_option].dtypes == 'object':
                    # st.write(df[categorical_option].value_counts())

                    # PAIRPLOT
                    st.subheader("Pairplot")
                    fig = sns.pairplot(df, hue=categorical_option)
                    st.pyplot(fig)

                    # COUNTPLOT
                    st.subheader("Countplot")
                    st.subheader(categorical_option)
                    fig, ax = plt.subplots()
                    ax = sns.countplot(data=df, x=categorical_option)
                    st.pyplot(fig)
                else:
                    st.write("Kolom yang Anda pilih tidak bertipe Kategorikal")

            st.write(
                "========================================================================")

            st.subheader("Correlation Map")

            st.dataframe(df.corr().style.highlight_max(axis=0))

            fig, ax = plt.subplots()
            ax = sns.heatmap(df.corr(), cmap='coolwarm', annot=True)
            st.pyplot(fig)

            st.write(
                "========================================================================")

            st.subheader("Describe Dataset")
            st.write(df.describe())

            st.write("Pilih kolom bertipe kategori untuk melihat grouping")
            group_option = st.selectbox('Choose group column:', df.columns)

            if st.button("Lihat Describe Group"):
                if df[group_option].dtypes == 'object':
                    st.dataframe(df.groupby(
                        group_option).describe().transpose())
                else:
                    st.write("**Tolong pilih atribut bertipe Kategorikal**")

            st.write(
                "========================================================================")

            st.subheader("Boxplot")
            st.write("""
                Salah satu fitur yang dipilih harus bertipe Kategori atau Numerik
            """)
            selected_fitur = st.multiselect('Pilih 2 Atribut:', df.columns)
            if st.button("Tampilkan Bloxplot"):
                fig, ax = plt.subplots()
                ax = sns.boxplot(
                    x=df[selected_fitur[0]], y=df[selected_fitur[1]], data=df, palette='winter')
                st.pyplot(fig)

            st.write(
                "========================================================================")

            st.subheader("Mean")
            mean_option = st.selectbox('Choose one column:', df.columns)
            if st.button("Tampilkan Mean"):
                if df[mean_option].dtypes == 'object':
                    st.write("""
                        Anda memilih kolom bertipe Kategorikal,
                        silahkan pilih kolom bertipa Numerik
                    """)
                else:
                    st.subheader(df[mean_option].mean())

    # UJI MODEL
    elif choice == "Uji Model":
        st.markdown('<style>h1{color: red;}</style>', unsafe_allow_html=True)
        st.title("Uji Model")
        st.markdown("""
            Prediksi yang dilakukan berdasarkan dataset yang digunakan saat ini.

            Jika Anda ingin menyesuaikan inputan dengan dataset Anda, anda dapat melakukan clone dan mengubah kode dari aplikasi
        """)
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
            st.dataframe(df_prediksi)
            selected_y = st.selectbox('Choose Target:', df_prediksi.columns)

            y = df_prediksi[selected_y]
            # st.write(y)
            X = df_prediksi.drop(selected_y, axis=1)

            sizing = [0.1, 0.2, 0.3]
            test_size = st.selectbox('Choose Test Size:', sizing)

            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=test_size, random_state=101)
            model = ['Decision Tree', 'Random Forest', 'Naive Bayes']
            selected_model = st.selectbox('Choose Model', model)
            # if st.button("Prediksi"):
            if selected_model == 'Decision Tree':
                # model_Decision_Tree(
                #     selected_model, X_train, X_test, y_train, y_test)
                decision_tree = model_Decision_Tree(
                    selected_model, X_train, X_test, y_train, y_test)
                prediksi_data_baru(decision_tree)
            elif selected_model == 'Random Forest':
                # model_Random_Forest(
                #     selected_model, X_train, X_test, y_train, y_test)
                random_forest = model_Random_Forest(
                    selected_model, X_train, X_test, y_train, y_test)
                prediksi_data_baru(random_forest)
            else:
                # model_Naive_Bayes(selected_model, X_train,
                #                   X_test, y_train, y_test)
                naive_bayes = model_Naive_Bayes(
                    selected_model, X_train, X_test, y_train, y_test)
                prediksi_data_baru(naive_bayes)

    # ABOUT
    else:
        st.markdown('<style>h1{color: red;}</style>', unsafe_allow_html=True)
        st.title("About")
        st.markdown("""
            Aplikasi dibuat untuk memenuhi tugas besar Digital Talent Incubation Telkom 2020.

            **Team**
            * DS0206 - Deva Hidayat
            * DS0210 - Gigas Taufan Arvyanto
            * DS0218 - Rachma Indira
        """)


if __name__ == "__main__":
    main()
