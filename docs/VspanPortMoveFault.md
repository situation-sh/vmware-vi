# VspanPortMoveFault

Thrown when moving a port used as tranmistted source or destination ports in vspan session to a promiscuous portgroup if this operation may change the non-promiscuous port to promiscuous mode.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**src_portgroup_name** | **str** | The key of the source portgroup.  ***Since:*** vSphere API 5.0  | 
**dest_portgroup_name** | **str** | The key of the dest portgroup.  ***Since:*** vSphere API 5.0  | 
**port_key** | **str** | The key of the port.  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.vspan_port_move_fault import VspanPortMoveFault

# TODO update the JSON string below
json = "{}"
# create an instance of VspanPortMoveFault from a JSON string
vspan_port_move_fault_instance = VspanPortMoveFault.from_json(json)
# print the JSON string representation of the object
print VspanPortMoveFault.to_json()

# convert the object into a dict
vspan_port_move_fault_dict = vspan_port_move_fault_instance.to_dict()
# create an instance of VspanPortMoveFault from a dict
vspan_port_move_fault_form_dict = vspan_port_move_fault.from_dict(vspan_port_move_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


