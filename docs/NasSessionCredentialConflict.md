# NasSessionCredentialConflict

This fault is thrown when an operation to configure a CIFS volume fails when attempting to log on more than once with the same user name.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**remote_host** | **str** | The host that runs the NFS server.  ***Since:*** vSphere API 4.0  | 
**remote_path** | **str** | The remote share.  ***Since:*** vSphere API 4.0  | 
**user_name** | **str** |  | 

## Example

```python
from vmware_vi.models.nas_session_credential_conflict import NasSessionCredentialConflict

# TODO update the JSON string below
json = "{}"
# create an instance of NasSessionCredentialConflict from a JSON string
nas_session_credential_conflict_instance = NasSessionCredentialConflict.from_json(json)
# print the JSON string representation of the object
print NasSessionCredentialConflict.to_json()

# convert the object into a dict
nas_session_credential_conflict_dict = nas_session_credential_conflict_instance.to_dict()
# create an instance of NasSessionCredentialConflict from a dict
nas_session_credential_conflict_form_dict = nas_session_credential_conflict.from_dict(nas_session_credential_conflict_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


