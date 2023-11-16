# ArrayOfSSLVerifyFault

A boxed array of *SSLVerifyFault*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[SSLVerifyFault]**](SSLVerifyFault.md) |  | 

## Example

```python
from vmware_vi.models.array_of_ssl_verify_fault import ArrayOfSSLVerifyFault

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfSSLVerifyFault from a JSON string
array_of_ssl_verify_fault_instance = ArrayOfSSLVerifyFault.from_json(json)
# print the JSON string representation of the object
print ArrayOfSSLVerifyFault.to_json()

# convert the object into a dict
array_of_ssl_verify_fault_dict = array_of_ssl_verify_fault_instance.to_dict()
# create an instance of ArrayOfSSLVerifyFault from a dict
array_of_ssl_verify_fault_form_dict = array_of_ssl_verify_fault.from_dict(array_of_ssl_verify_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


