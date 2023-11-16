# ArrayOfSSPIAuthentication

A boxed array of *SSPIAuthentication*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[SSPIAuthentication]**](SSPIAuthentication.md) |  | 

## Example

```python
from vmware_vi.models.array_of_sspi_authentication import ArrayOfSSPIAuthentication

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfSSPIAuthentication from a JSON string
array_of_sspi_authentication_instance = ArrayOfSSPIAuthentication.from_json(json)
# print the JSON string representation of the object
print ArrayOfSSPIAuthentication.to_json()

# convert the object into a dict
array_of_sspi_authentication_dict = array_of_sspi_authentication_instance.to_dict()
# create an instance of ArrayOfSSPIAuthentication from a dict
array_of_sspi_authentication_form_dict = array_of_sspi_authentication.from_dict(array_of_sspi_authentication_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


