# IncorrectHostInformation

A IncorrectHostInformation is thrown if the host does not provide the information needed to acquire the correct set of licenses.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.incorrect_host_information import IncorrectHostInformation

# TODO update the JSON string below
json = "{}"
# create an instance of IncorrectHostInformation from a JSON string
incorrect_host_information_instance = IncorrectHostInformation.from_json(json)
# print the JSON string representation of the object
print IncorrectHostInformation.to_json()

# convert the object into a dict
incorrect_host_information_dict = incorrect_host_information_instance.to_dict()
# create an instance of IncorrectHostInformation from a dict
incorrect_host_information_form_dict = incorrect_host_information.from_dict(incorrect_host_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


