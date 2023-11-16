# ArrayOfOvfImport

A boxed array of *OvfImport*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[OvfImport]**](OvfImport.md) |  | 

## Example

```python
from vmware_vi.models.array_of_ovf_import import ArrayOfOvfImport

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfOvfImport from a JSON string
array_of_ovf_import_instance = ArrayOfOvfImport.from_json(json)
# print the JSON string representation of the object
print ArrayOfOvfImport.to_json()

# convert the object into a dict
array_of_ovf_import_dict = array_of_ovf_import_instance.to_dict()
# create an instance of ArrayOfOvfImport from a dict
array_of_ovf_import_form_dict = array_of_ovf_import.from_dict(array_of_ovf_import_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


