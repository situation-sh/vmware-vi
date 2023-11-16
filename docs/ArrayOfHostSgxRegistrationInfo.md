# ArrayOfHostSgxRegistrationInfo

A boxed array of *HostSgxRegistrationInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostSgxRegistrationInfo]**](HostSgxRegistrationInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_sgx_registration_info import ArrayOfHostSgxRegistrationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostSgxRegistrationInfo from a JSON string
array_of_host_sgx_registration_info_instance = ArrayOfHostSgxRegistrationInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostSgxRegistrationInfo.to_json()

# convert the object into a dict
array_of_host_sgx_registration_info_dict = array_of_host_sgx_registration_info_instance.to_dict()
# create an instance of ArrayOfHostSgxRegistrationInfo from a dict
array_of_host_sgx_registration_info_form_dict = array_of_host_sgx_registration_info.from_dict(array_of_host_sgx_registration_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


