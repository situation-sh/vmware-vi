# DvsPortVendorSpecificStateChangeEvent

A port of which vendor specific state is changed in the vNetwork Distributed Switch.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**port_key** | **str** | The port key.  ***Since:*** vSphere API 5.1  | 

## Example

```python
from vmware_vi.models.dvs_port_vendor_specific_state_change_event import DvsPortVendorSpecificStateChangeEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DvsPortVendorSpecificStateChangeEvent from a JSON string
dvs_port_vendor_specific_state_change_event_instance = DvsPortVendorSpecificStateChangeEvent.from_json(json)
# print the JSON string representation of the object
print DvsPortVendorSpecificStateChangeEvent.to_json()

# convert the object into a dict
dvs_port_vendor_specific_state_change_event_dict = dvs_port_vendor_specific_state_change_event_instance.to_dict()
# create an instance of DvsPortVendorSpecificStateChangeEvent from a dict
dvs_port_vendor_specific_state_change_event_form_dict = dvs_port_vendor_specific_state_change_event.from_dict(dvs_port_vendor_specific_state_change_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


