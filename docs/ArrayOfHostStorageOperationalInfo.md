# ArrayOfHostStorageOperationalInfo

A boxed array of *HostStorageOperationalInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostStorageOperationalInfo]**](HostStorageOperationalInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_storage_operational_info import ArrayOfHostStorageOperationalInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostStorageOperationalInfo from a JSON string
array_of_host_storage_operational_info_instance = ArrayOfHostStorageOperationalInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostStorageOperationalInfo.to_json()

# convert the object into a dict
array_of_host_storage_operational_info_dict = array_of_host_storage_operational_info_instance.to_dict()
# create an instance of ArrayOfHostStorageOperationalInfo from a dict
array_of_host_storage_operational_info_form_dict = array_of_host_storage_operational_info.from_dict(array_of_host_storage_operational_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


