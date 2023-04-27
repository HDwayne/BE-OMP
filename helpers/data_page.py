import streamlit as st
from helpers.utils import *


def main():
    # ---------------------------- SIDEBAR -------------------------------- #
    print_widgets_separator(1, sidebar=True)
    
    file = st.sidebar.file_uploader(label='Ajouter un fichier',
                                     accept_multiple_files=False,
                                     type=['zip'])
    
    if file is not None:
        if not CheckZipFileName(file.name):
            st.sidebar.error('Le nom du fichier ne respecte pas la syntaxe')
        else:
            delete_session_state_rule(checkFileName)

            added_file = []
            dfs = read_zip_file(file)
            apply_time_dfs(dfs, ['20t_Date'], "%d/%m/%Y,%H:%M:%S")
            for key, value in dfs.items():
                added_file.append(key)
                if not key in st.session_state:
                    st.session_state[key] = value
                else:
                    st.session_state[key] = st.session_state[key]

            st.sidebar.success(f'Les fichiers suivants ont été ajoutés : {", ".join(added_file)}')
            
    # ------------------------- PAGE CONTENT ----------------------------- #
    
    st.header('Données enregistrées')

    number_file = getNumberFileImpoted()
    if number_file == 0:
        st.info('Aucune donnée enregistré, veuillez importer un fichier zip depuis la section de gauche.')
    elif number_file != 5:
        st.warning('Le fichier zip utilisé ne contient pas le nombre de fichiers attendus. certaines fonctionnalités sont susceptibles de ne pas fonctionner correctement.')
    else:

        tab1, tab2= st.tabs(["TEI48", "TEI49"])

        for key, value in st.session_state.items():
            if checkFileName(key, contain_date=False):
                if "TEI48" in key:
                    tab1.subheader(key)
                    tab1.write(value)
                elif "TEI49" in key:
                    tab2.subheader(key)
                    tab2.write(value)
            


    

    