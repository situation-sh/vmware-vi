# HostSerialAttachedTargetTransport

Serial attached adapter transport information about a SCSI target.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.host_serial_attached_target_transport import HostSerialAttachedTargetTransport

# TODO update the JSON string below
json = "{}"
# create an instance of HostSerialAttachedTargetTransport from a JSON string
host_serial_attached_target_transport_instance = HostSerialAttachedTargetTransport.from_json(json)
# print the JSON string representation of the object
print HostSerialAttachedTargetTransport.to_json()

# convert the object into a dict
host_serial_attached_target_transport_dict = host_serial_attached_target_transport_instance.to_dict()
# create an instance of HostSerialAttachedTargetTransport from a dict
host_serial_attached_target_transport_form_dict = host_serial_attached_target_transport.from_dict(host_serial_attached_target_transport_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


