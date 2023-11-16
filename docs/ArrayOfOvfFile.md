# ArrayOfOvfFile

A boxed array of *OvfFile*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[OvfFile]**](OvfFile.md) |  | 

## Example

```python
from vmware_vi.models.array_of_ovf_file import ArrayOfOvfFile

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfOvfFile from a JSON string
array_of_ovf_file_instance = ArrayOfOvfFile.from_json(json)
# print the JSON string representation of the object
print ArrayOfOvfFile.to_json()

# convert the object into a dict
array_of_ovf_file_dict = array_of_ovf_file_instance.to_dict()
# create an instance of ArrayOfOvfFile from a dict
array_of_ovf_file_form_dict = array_of_ovf_file.from_dict(array_of_ovf_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


