# ArrayOfSSLDisabledFault

A boxed array of *SSLDisabledFault*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[SSLDisabledFault]**](SSLDisabledFault.md) |  | 

## Example

```python
from vmware_vi.models.array_of_ssl_disabled_fault import ArrayOfSSLDisabledFault

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfSSLDisabledFault from a JSON string
array_of_ssl_disabled_fault_instance = ArrayOfSSLDisabledFault.from_json(json)
# print the JSON string representation of the object
print ArrayOfSSLDisabledFault.to_json()

# convert the object into a dict
array_of_ssl_disabled_fault_dict = array_of_ssl_disabled_fault_instance.to_dict()
# create an instance of ArrayOfSSLDisabledFault from a dict
array_of_ssl_disabled_fault_form_dict = array_of_ssl_disabled_fault.from_dict(array_of_ssl_disabled_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


