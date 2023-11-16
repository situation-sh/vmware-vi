# HostNasVolumeSecurityTypeEnum

Security type supported.  Possible values: - `AUTH_SYS`: Authentication based on traditional UNIX identifiers (UID and GID).      Server trusts the IDs sent by the client for each request and uses them   to perform access control. Current implementation only supports   AUTH\\_SYS with root user. - `SEC_KRB5`: Ensures RPC header authentication using Kerberos session keys.      When   this option is enabled, the client uses the information specified in   *HostNasVolumeUserInfo* to establish shared keys with the server using   Kerberos. These shared keys are used to generate and verify message   authentication codes for RPC header of NFS requests and responses,   respectively. This method does not secure NFS file data. - `SEC_KRB5I`: Extends SEC\\_KRB5 to generate and verify message authentication codes   for the payload of NFS requests and responses respectively.      This   ensures the integrity of the NFS file data.      ***Since:*** vSphere API 6.5  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


