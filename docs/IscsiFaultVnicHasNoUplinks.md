# IscsiFaultVnicHasNoUplinks

This fault indicates the given Virtual NIC has no uplinks and not suitable for iSCSI multi-pathing configuration.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vnic_device** | **str** |  | 

## Example

```python
from vmware_vi.models.iscsi_fault_vnic_has_no_uplinks import IscsiFaultVnicHasNoUplinks

# TODO update the JSON string below
json = "{}"
# create an instance of IscsiFaultVnicHasNoUplinks from a JSON string
iscsi_fault_vnic_has_no_uplinks_instance = IscsiFaultVnicHasNoUplinks.from_json(json)
# print the JSON string representation of the object
print IscsiFaultVnicHasNoUplinks.to_json()

# convert the object into a dict
iscsi_fault_vnic_has_no_uplinks_dict = iscsi_fault_vnic_has_no_uplinks_instance.to_dict()
# create an instance of IscsiFaultVnicHasNoUplinks from a dict
iscsi_fault_vnic_has_no_uplinks_form_dict = iscsi_fault_vnic_has_no_uplinks.from_dict(iscsi_fault_vnic_has_no_uplinks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


