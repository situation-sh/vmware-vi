# ScsiLunCapabilities

Scsi device specific capabilities.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**update_display_name_supported** | **bool** | Can the display name of the SCSI device be updated?  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.scsi_lun_capabilities import ScsiLunCapabilities

# TODO update the JSON string below
json = "{}"
# create an instance of ScsiLunCapabilities from a JSON string
scsi_lun_capabilities_instance = ScsiLunCapabilities.from_json(json)
# print the JSON string representation of the object
print ScsiLunCapabilities.to_json()

# convert the object into a dict
scsi_lun_capabilities_dict = scsi_lun_capabilities_instance.to_dict()
# create an instance of ScsiLunCapabilities from a dict
scsi_lun_capabilities_form_dict = scsi_lun_capabilities.from_dict(scsi_lun_capabilities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


