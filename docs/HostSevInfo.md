# HostSevInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sev_state** | **str** | State of SEV on the host.  The set of supported values are described in *HostSevInfoSevState_enum*.  ***Since:*** vSphere API 7.0.1.0  | 
**max_sev_es_guests** | **int** | The maximum number of SEV-ES guests supported on this host.  ***Since:*** vSphere API 7.0.1.0  | 

## Example

```python
from vmware_vi.models.host_sev_info import HostSevInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostSevInfo from a JSON string
host_sev_info_instance = HostSevInfo.from_json(json)
# print the JSON string representation of the object
print HostSevInfo.to_json()

# convert the object into a dict
host_sev_info_dict = host_sev_info_instance.to_dict()
# create an instance of HostSevInfo from a dict
host_sev_info_form_dict = host_sev_info.from_dict(host_sev_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


