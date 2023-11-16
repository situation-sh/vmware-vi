# ArrayOfHostAuthenticationStoreInfo

A boxed array of *HostAuthenticationStoreInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostAuthenticationStoreInfo]**](HostAuthenticationStoreInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_authentication_store_info import ArrayOfHostAuthenticationStoreInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostAuthenticationStoreInfo from a JSON string
array_of_host_authentication_store_info_instance = ArrayOfHostAuthenticationStoreInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostAuthenticationStoreInfo.to_json()

# convert the object into a dict
array_of_host_authentication_store_info_dict = array_of_host_authentication_store_info_instance.to_dict()
# create an instance of ArrayOfHostAuthenticationStoreInfo from a dict
array_of_host_authentication_store_info_form_dict = array_of_host_authentication_store_info.from_dict(array_of_host_authentication_store_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


