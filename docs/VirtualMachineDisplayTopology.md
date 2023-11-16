# VirtualMachineDisplayTopology

This data object defines a two-dimensional, rectangular display area.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**x** | **int** | The x co-ordinate defining the start of the display rectangle.  ***Since:*** vSphere API 4.0  | 
**y** | **int** | The y co-ordinate defining the start of the display rectangle.  ***Since:*** vSphere API 4.0  | 
**width** | **int** | The width of the display rectangle.  ***Since:*** vSphere API 4.0  | 
**height** | **int** | The height of the display rectangle.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.virtual_machine_display_topology import VirtualMachineDisplayTopology

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineDisplayTopology from a JSON string
virtual_machine_display_topology_instance = VirtualMachineDisplayTopology.from_json(json)
# print the JSON string representation of the object
print VirtualMachineDisplayTopology.to_json()

# convert the object into a dict
virtual_machine_display_topology_dict = virtual_machine_display_topology_instance.to_dict()
# create an instance of VirtualMachineDisplayTopology from a dict
virtual_machine_display_topology_form_dict = virtual_machine_display_topology.from_dict(virtual_machine_display_topology_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


