# DVSManagerLookupDvPortGroupRequestType

The parameters of *DistributedVirtualSwitchManager.DVSManagerLookupDvPortGroup*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**switch_uuid** | **str** | The UUID of the *DistributedVirtualSwitch*.  | 
**portgroup_key** | **str** | The key that identifies a *DistributedVirtualPortgroup*.  | 

## Example

```python
from vmware_vi.models.dvs_manager_lookup_dv_port_group_request_type import DVSManagerLookupDvPortGroupRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of DVSManagerLookupDvPortGroupRequestType from a JSON string
dvs_manager_lookup_dv_port_group_request_type_instance = DVSManagerLookupDvPortGroupRequestType.from_json(json)
# print the JSON string representation of the object
print DVSManagerLookupDvPortGroupRequestType.to_json()

# convert the object into a dict
dvs_manager_lookup_dv_port_group_request_type_dict = dvs_manager_lookup_dv_port_group_request_type_instance.to_dict()
# create an instance of DVSManagerLookupDvPortGroupRequestType from a dict
dvs_manager_lookup_dv_port_group_request_type_form_dict = dvs_manager_lookup_dv_port_group_request_type.from_dict(dvs_manager_lookup_dv_port_group_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


