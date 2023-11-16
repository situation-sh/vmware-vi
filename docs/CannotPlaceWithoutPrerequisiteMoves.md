# CannotPlaceWithoutPrerequisiteMoves

This fault is thrown when Storage DRS cannot recommend to place disks of a virtual machine without moving existing virtual disks in a datastore cluster.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.cannot_place_without_prerequisite_moves import CannotPlaceWithoutPrerequisiteMoves

# TODO update the JSON string below
json = "{}"
# create an instance of CannotPlaceWithoutPrerequisiteMoves from a JSON string
cannot_place_without_prerequisite_moves_instance = CannotPlaceWithoutPrerequisiteMoves.from_json(json)
# print the JSON string representation of the object
print CannotPlaceWithoutPrerequisiteMoves.to_json()

# convert the object into a dict
cannot_place_without_prerequisite_moves_dict = cannot_place_without_prerequisite_moves_instance.to_dict()
# create an instance of CannotPlaceWithoutPrerequisiteMoves from a dict
cannot_place_without_prerequisite_moves_form_dict = cannot_place_without_prerequisite_moves.from_dict(cannot_place_without_prerequisite_moves_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


