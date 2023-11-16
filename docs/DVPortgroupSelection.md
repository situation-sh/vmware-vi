# DVPortgroupSelection

Class to specify selection criteria of list of vNetwork Distributed Portgroups.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dvs_uuid** | **str** | vSphere Distributed Switch uuid  ***Since:*** vSphere API 5.0  | 
**portgroup_key** | **List[str]** | List of vNetwork Distributed Portgroup keys  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.dv_portgroup_selection import DVPortgroupSelection

# TODO update the JSON string below
json = "{}"
# create an instance of DVPortgroupSelection from a JSON string
dv_portgroup_selection_instance = DVPortgroupSelection.from_json(json)
# print the JSON string representation of the object
print DVPortgroupSelection.to_json()

# convert the object into a dict
dv_portgroup_selection_dict = dv_portgroup_selection_instance.to_dict()
# create an instance of DVPortgroupSelection from a dict
dv_portgroup_selection_form_dict = dv_portgroup_selection.from_dict(dv_portgroup_selection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


