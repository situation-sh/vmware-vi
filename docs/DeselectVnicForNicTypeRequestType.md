# DeselectVnicForNicTypeRequestType

The parameters of *HostVirtualNicManager.DeselectVnicForNicType*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nic_type** | **str** | The type of VirtualNic that would be deselected  | 
**device** | **str** | The device that uniquely identifies the VirtualNic.  | 

## Example

```python
from vmware_vi.models.deselect_vnic_for_nic_type_request_type import DeselectVnicForNicTypeRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of DeselectVnicForNicTypeRequestType from a JSON string
deselect_vnic_for_nic_type_request_type_instance = DeselectVnicForNicTypeRequestType.from_json(json)
# print the JSON string representation of the object
print DeselectVnicForNicTypeRequestType.to_json()

# convert the object into a dict
deselect_vnic_for_nic_type_request_type_dict = deselect_vnic_for_nic_type_request_type_instance.to_dict()
# create an instance of DeselectVnicForNicTypeRequestType from a dict
deselect_vnic_for_nic_type_request_type_form_dict = deselect_vnic_for_nic_type_request_type.from_dict(deselect_vnic_for_nic_type_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


