# ArrayOfVolumeEditorError

A boxed array of *VolumeEditorError*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VolumeEditorError]**](VolumeEditorError.md) |  | 

## Example

```python
from vmware_vi.models.array_of_volume_editor_error import ArrayOfVolumeEditorError

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVolumeEditorError from a JSON string
array_of_volume_editor_error_instance = ArrayOfVolumeEditorError.from_json(json)
# print the JSON string representation of the object
print ArrayOfVolumeEditorError.to_json()

# convert the object into a dict
array_of_volume_editor_error_dict = array_of_volume_editor_error_instance.to_dict()
# create an instance of ArrayOfVolumeEditorError from a dict
array_of_volume_editor_error_form_dict = array_of_volume_editor_error.from_dict(array_of_volume_editor_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


