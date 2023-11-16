# VspanPortgroupPromiscChangeFault

Thrown when changing a non-promiscous portgroup to promiscuous mode if any port in this portgroup is used as tranmistted source or dest ports in vspan session.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**portgroup_name** | **str** | The key of the port.  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.vspan_portgroup_promisc_change_fault import VspanPortgroupPromiscChangeFault

# TODO update the JSON string below
json = "{}"
# create an instance of VspanPortgroupPromiscChangeFault from a JSON string
vspan_portgroup_promisc_change_fault_instance = VspanPortgroupPromiscChangeFault.from_json(json)
# print the JSON string representation of the object
print VspanPortgroupPromiscChangeFault.to_json()

# convert the object into a dict
vspan_portgroup_promisc_change_fault_dict = vspan_portgroup_promisc_change_fault_instance.to_dict()
# create an instance of VspanPortgroupPromiscChangeFault from a dict
vspan_portgroup_promisc_change_fault_form_dict = vspan_portgroup_promisc_change_fault.from_dict(vspan_portgroup_promisc_change_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


