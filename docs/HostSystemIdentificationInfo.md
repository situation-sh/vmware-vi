# HostSystemIdentificationInfo

This data object describes system identifying information of the host.  This information may be vendor specific.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier_value** | **str** | The system identification information  ***Since:*** VI API 2.5  | 
**identifier_type** | [**ElementDescription**](ElementDescription.md) |  | 

## Example

```python
from vmware_vi.models.host_system_identification_info import HostSystemIdentificationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostSystemIdentificationInfo from a JSON string
host_system_identification_info_instance = HostSystemIdentificationInfo.from_json(json)
# print the JSON string representation of the object
print HostSystemIdentificationInfo.to_json()

# convert the object into a dict
host_system_identification_info_dict = host_system_identification_info_instance.to_dict()
# create an instance of HostSystemIdentificationInfo from a dict
host_system_identification_info_form_dict = host_system_identification_info.from_dict(host_system_identification_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


