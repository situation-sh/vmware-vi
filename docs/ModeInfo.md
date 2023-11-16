# ModeInfo

The FileAccess.Modes data object type defines the known access modes for a datastore.  The property values specify how to interpret the \"what\" property for a FileAccess object. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**browse** | **str** | Can see the existence of a file.  | [optional] 
**read** | **str** | Can read a file.  | 
**modify** | **str** | Can read and write a file.  | 
**use** | **str** | Can execute or operate a file or look inside a directory.  | 
**admin** | **str** | Can change permissions for a file.  | [optional] 
**full** | **str** | Can do anything to a file, including change permissions.  | 

## Example

```python
from vmware_vi.models.mode_info import ModeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ModeInfo from a JSON string
mode_info_instance = ModeInfo.from_json(json)
# print the JSON string representation of the object
print ModeInfo.to_json()

# convert the object into a dict
mode_info_dict = mode_info_instance.to_dict()
# create an instance of ModeInfo from a dict
mode_info_form_dict = mode_info.from_dict(mode_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


