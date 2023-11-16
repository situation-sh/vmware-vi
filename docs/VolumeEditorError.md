# VolumeEditorError

An error occurred in the Open Source Components applications during volume editing.  Possibly caused by an incompatible cygwin version installed in the VirtualCenter server. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.volume_editor_error import VolumeEditorError

# TODO update the JSON string below
json = "{}"
# create an instance of VolumeEditorError from a JSON string
volume_editor_error_instance = VolumeEditorError.from_json(json)
# print the JSON string representation of the object
print VolumeEditorError.to_json()

# convert the object into a dict
volume_editor_error_dict = volume_editor_error_instance.to_dict()
# create an instance of VolumeEditorError from a dict
volume_editor_error_form_dict = volume_editor_error.from_dict(volume_editor_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


