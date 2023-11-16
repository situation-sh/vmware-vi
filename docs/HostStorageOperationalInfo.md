# HostStorageOperationalInfo

Data class describing operational information of a storage element  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_property** | **str** | The property of interest for the storage element  ***Since:*** VI API 2.5  | 
**value** | **str** | The property value for the storage element  ***Since:*** VI API 2.5  | 

## Example

```python
from vmware_vi.models.host_storage_operational_info import HostStorageOperationalInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostStorageOperationalInfo from a JSON string
host_storage_operational_info_instance = HostStorageOperationalInfo.from_json(json)
# print the JSON string representation of the object
print HostStorageOperationalInfo.to_json()

# convert the object into a dict
host_storage_operational_info_dict = host_storage_operational_info_instance.to_dict()
# create an instance of HostStorageOperationalInfo from a dict
host_storage_operational_info_form_dict = host_storage_operational_info.from_dict(host_storage_operational_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


