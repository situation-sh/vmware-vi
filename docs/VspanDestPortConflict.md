# VspanDestPortConflict

Thrown if a dvPort is used as destination in multiple Distributed Port Mirroring sessions.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vspan_session_key1** | **str** | The key of the Distributed Port Mirroring session whose destination ports include a port that is also used as destination ports of other Distributed Port Mirroring sessions  ***Since:*** vSphere API 5.0  | 
**vspan_session_key2** | **str** | The key of the Distributed Port Mirroring session whose destination ports include a port that is also used as destination ports of other Distributed Port Mirroring sessions  ***Since:*** vSphere API 5.0  | 
**port_key** | **str** | The key of the the port that is used as destination in multiple Distributed Port Mirroring sessions  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.vspan_dest_port_conflict import VspanDestPortConflict

# TODO update the JSON string below
json = "{}"
# create an instance of VspanDestPortConflict from a JSON string
vspan_dest_port_conflict_instance = VspanDestPortConflict.from_json(json)
# print the JSON string representation of the object
print VspanDestPortConflict.to_json()

# convert the object into a dict
vspan_dest_port_conflict_dict = vspan_dest_port_conflict_instance.to_dict()
# create an instance of VspanDestPortConflict from a dict
vspan_dest_port_conflict_form_dict = vspan_dest_port_conflict.from_dict(vspan_dest_port_conflict_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


