import steamlit as st

def check_malicious():
    starts_cmd = st.checkbox("Starts CMD.EXE for commands execution")
    creates_files_user = st.checkbox("Creates files in the user directory")
    creates_files_program = st.checkbox("Creates files in the program directory")
    spawns_vssadmin = st.checkbox("Spawns vssadmin.exe")
    spawns_wmic = st.checkbox("Spawns wmic.exe")
    registry_reads = st.multiselect("Select the registry reads",
                                    ["HKEY_LOCAL_MACHINE\SYSTEM\CONTROLSET001\CONTROL\NLS\SORTING\VERSIONS",
                                     "HKEY_LOCAL_MACHINE\SYSTEM\CONTROLSET001\CONTROL\COMPUTERNAME\ACTIVECOMPUTERNAME",
                                     "HKEY_LOCAL_MACHINE\SOFTWARE\MICROSOFT\CRYPTOGRAPHY",
                                     "HKEY_LOCAL_MACHINE\SYSTEM\CONTROLSET001\CONTROL\LSA\FIPSALGORITHMPOLICY",
                                     "HKEY_LOCAL_MACHINE\SOFTWARE\MICROSOFT\WINDOWS NT\CURRENTVERSION"])

    if any([starts_cmd, creates_files_user, creates_files_program, spawns_vssadmin, spawns_wmic]) and any(
            ["HKEY_LOCAL_MACHINE\SYSTEM\CONTROLSET001\CONTROL\NLS\SORTING\VERSIONS" in registry_reads,
             "HKEY_LOCAL_MACHINE\SYSTEM\CONTROLSET001\CONTROL\COMPUTERNAME\ACTIVECOMPUTERNAME" in registry_reads,
             "HKEY_LOCAL_MACHINE\SOFTWARE\MICROSOFT\CRYPTOGRAPHY" in registry_reads,
             "HKEY_LOCAL_MACHINE\SYSTEM\CONTROLSET001\CONTROL\LSA\FIPSALGORITHMPOLICY" in registry_reads,
             "HKEY_LOCAL_MACHINE\SOFTWARE\MICROSOFT\WINDOWS NT\CURRENTVERSION" in registry_reads]):
        st.warning("Process might be a Ransomeware")
    elif all(["HKEY_CURRENT_USER\SOFTWARE\MICROSOFT\WINDOWS\CURRENTVERSION\INTERNET SETTINGS" in registry_reads,
              "HKEY_LOCAL_MACHINE\SOFTWARE\MICROSOFT\CRYPTOGRAPHY" in registry_reads,
              "HKEY_LOCAL_MACHINE\SYSTEM\CONTROLSET001\CONTROL\COMPUTERNAME\ACTIVECOMPUTERNAME" in registry_reads,
              "HKEY_LOCAL_MACHINE\SYSTEM\CONTROLSET001\CONTROL\LSA\FIPSALGORITHMPOLICY" in registry_reads,
              "HKEY_LOCAL_MACHINE\SYSTEM\CONTROLSET001\CONTROL\NLS\SORTING\VERSIONS" in registry_reads,
              "HKEY_CURRENT_USER\SOFTWARE\MICROSOFT\WINDOWS\CURRENTVERSION\INTERNET SETTINGS" in registry_reads]):
        st.warning("Process might be cobalt strike")
    else:
        st.success("Process is not known to be malicious")

st.title("Malicious Process Detector")
check_malicious()


