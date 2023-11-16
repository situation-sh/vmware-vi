# HostInternetScsiTargetTransport

Internet SCSI transport information about a SCSI target. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**i_scsi_name** | **str** | The iSCSI name of the target.  | 
**i_scsi_alias** | **str** | The iSCSI alias of the target.  | 
**address** | **List[str]** | The IP addresses through which the target may be reached.  | [optional] 

## Example

```python
from vmware_vi.models.host_internet_scsi_target_transport import HostInternetScsiTargetTransport

# TODO update the JSON string below
json = "{}"
# create an instance of HostInternetScsiTargetTransport from a JSON string
host_internet_scsi_target_transport_instance = HostInternetScsiTargetTransport.from_json(json)
# print the JSON string representation of the object
print HostInternetScsiTargetTransport.to_json()

# convert the object into a dict
host_internet_scsi_target_transport_dict = host_internet_scsi_target_transport_instance.to_dict()
# create an instance of HostInternetScsiTargetTransport from a dict
host_internet_scsi_target_transport_form_dict = host_internet_scsi_target_transport.from_dict(host_internet_scsi_target_transport_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


