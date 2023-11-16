# VspanPortgroupTypeChangeFault

Thrown when changing a portgroup from static/dynamic binding to ephemeral(no binding) if any ports in this portgroup participate in Distributed Port Mirroring session.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**portgroup_name** | **str** | The name of the portgroup.  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.vspan_portgroup_type_change_fault import VspanPortgroupTypeChangeFault

# TODO update the JSON string below
json = "{}"
# create an instance of VspanPortgroupTypeChangeFault from a JSON string
vspan_portgroup_type_change_fault_instance = VspanPortgroupTypeChangeFault.from_json(json)
# print the JSON string representation of the object
print VspanPortgroupTypeChangeFault.to_json()

# convert the object into a dict
vspan_portgroup_type_change_fault_dict = vspan_portgroup_type_change_fault_instance.to_dict()
# create an instance of VspanPortgroupTypeChangeFault from a dict
vspan_portgroup_type_change_fault_form_dict = vspan_portgroup_type_change_fault.from_dict(vspan_portgroup_type_change_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


