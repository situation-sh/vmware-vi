# VMOnConflictDVPort

The virtual machine is using a conflict DVPort, which is a temporary port created to avoid conflict with another port.  Conflict DVPort cannot be moved.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vmon_conflict_dv_port import VMOnConflictDVPort

# TODO update the JSON string below
json = "{}"
# create an instance of VMOnConflictDVPort from a JSON string
vmon_conflict_dv_port_instance = VMOnConflictDVPort.from_json(json)
# print the JSON string representation of the object
print VMOnConflictDVPort.to_json()

# convert the object into a dict
vmon_conflict_dv_port_dict = vmon_conflict_dv_port_instance.to_dict()
# create an instance of VMOnConflictDVPort from a dict
vmon_conflict_dv_port_form_dict = vmon_conflict_dv_port.from_dict(vmon_conflict_dv_port_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


