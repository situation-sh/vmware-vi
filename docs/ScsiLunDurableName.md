# ScsiLunDurableName

This data object type represents an SMI-S \"Correlatable and Durable Name\" which is an identifier for a logical unit number (LUN) that is generated using a common algorithm.  The algorithm divides the identifier into multiple namespaces where each namespace uses a different set of properties of the LUN to generate the identifier. The namespace itself is encoded in the identifier. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**namespace** | **str** | The string describing the namespace used for the durable name.  | 
**namespace_id** | **int** | The byte used by the ESX Server product to represent the namespace.  | 
**data** | **List[int]** | The variable length byte array containing the namespace-specific data.  For a SCSI-3 compliant device this field is the descriptor header along with the payload for data obtained from page 83h, and is the payload for data obtained from page 80h of the Vital Product Data (VPD).  | [optional] 

## Example

```python
from vmware_vi.models.scsi_lun_durable_name import ScsiLunDurableName

# TODO update the JSON string below
json = "{}"
# create an instance of ScsiLunDurableName from a JSON string
scsi_lun_durable_name_instance = ScsiLunDurableName.from_json(json)
# print the JSON string representation of the object
print ScsiLunDurableName.to_json()

# convert the object into a dict
scsi_lun_durable_name_dict = scsi_lun_durable_name_instance.to_dict()
# create an instance of ScsiLunDurableName from a dict
scsi_lun_durable_name_form_dict = scsi_lun_durable_name.from_dict(scsi_lun_durable_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


