# ArrayOfHostLicensableResourceInfo

A boxed array of *HostLicensableResourceInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostLicensableResourceInfo]**](HostLicensableResourceInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_licensable_resource_info import ArrayOfHostLicensableResourceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostLicensableResourceInfo from a JSON string
array_of_host_licensable_resource_info_instance = ArrayOfHostLicensableResourceInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostLicensableResourceInfo.to_json()

# convert the object into a dict
array_of_host_licensable_resource_info_dict = array_of_host_licensable_resource_info_instance.to_dict()
# create an instance of ArrayOfHostLicensableResourceInfo from a dict
array_of_host_licensable_resource_info_form_dict = array_of_host_licensable_resource_info.from_dict(array_of_host_licensable_resource_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


