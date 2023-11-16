# BindVnicRequestType

The parameters of *IscsiManager.BindVnic*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**i_scsi_hba_name** | **str** | iSCSI adapter name for which the Virtual NIC to be added.  | 
**vnic_device** | **str** | Virtual NIC that is to be bound to the iSCSI HBA  | 

## Example

```python
from vmware_vi.models.bind_vnic_request_type import BindVnicRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of BindVnicRequestType from a JSON string
bind_vnic_request_type_instance = BindVnicRequestType.from_json(json)
# print the JSON string representation of the object
print BindVnicRequestType.to_json()

# convert the object into a dict
bind_vnic_request_type_dict = bind_vnic_request_type_instance.to_dict()
# create an instance of BindVnicRequestType from a dict
bind_vnic_request_type_form_dict = bind_vnic_request_type.from_dict(bind_vnic_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


