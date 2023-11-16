# MaintenanceModeFileMove

Migration of the virtual machine to the target host will need a move of virtual machine files, like configuration file or virtual disks, which is not permitted if the source host is in maintenance mode.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.maintenance_mode_file_move import MaintenanceModeFileMove

# TODO update the JSON string below
json = "{}"
# create an instance of MaintenanceModeFileMove from a JSON string
maintenance_mode_file_move_instance = MaintenanceModeFileMove.from_json(json)
# print the JSON string representation of the object
print MaintenanceModeFileMove.to_json()

# convert the object into a dict
maintenance_mode_file_move_dict = maintenance_mode_file_move_instance.to_dict()
# create an instance of MaintenanceModeFileMove from a dict
maintenance_mode_file_move_form_dict = maintenance_mode_file_move.from_dict(maintenance_mode_file_move_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


