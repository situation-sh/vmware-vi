# ArrayOfIncorrectHostInformation

A boxed array of *IncorrectHostInformation*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[IncorrectHostInformation]**](IncorrectHostInformation.md) |  | 

## Example

```python
from vmware_vi.models.array_of_incorrect_host_information import ArrayOfIncorrectHostInformation

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfIncorrectHostInformation from a JSON string
array_of_incorrect_host_information_instance = ArrayOfIncorrectHostInformation.from_json(json)
# print the JSON string representation of the object
print ArrayOfIncorrectHostInformation.to_json()

# convert the object into a dict
array_of_incorrect_host_information_dict = array_of_incorrect_host_information_instance.to_dict()
# create an instance of ArrayOfIncorrectHostInformation from a dict
array_of_incorrect_host_information_form_dict = array_of_incorrect_host_information.from_dict(array_of_incorrect_host_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


