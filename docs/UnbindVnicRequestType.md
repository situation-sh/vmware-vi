# UnbindVnicRequestType

The parameters of *IscsiManager.UnbindVnic*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**i_scsi_hba_name** | **str** | iSCSI adapter name for which the Virtual NIC to be removed.  | 
**vnic_device** | **str** | Virtual NIC that is to be removed from the iSCSI HBA  | 
**force** | **bool** |  | 

## Example

```python
from vmware_vi.models.unbind_vnic_request_type import UnbindVnicRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UnbindVnicRequestType from a JSON string
unbind_vnic_request_type_instance = UnbindVnicRequestType.from_json(json)
# print the JSON string representation of the object
print UnbindVnicRequestType.to_json()

# convert the object into a dict
unbind_vnic_request_type_dict = unbind_vnic_request_type_instance.to_dict()
# create an instance of UnbindVnicRequestType from a dict
unbind_vnic_request_type_form_dict = unbind_vnic_request_type.from_dict(unbind_vnic_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


