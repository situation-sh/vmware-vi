# DVSVendorSpecificConfig

This data object type describes vendor specific configuration.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_value** | [**List[DistributedVirtualSwitchKeyedOpaqueBlob]**](DistributedVirtualSwitchKeyedOpaqueBlob.md) | An opaque binary blob that stores vendor specific configuration.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.dvs_vendor_specific_config import DVSVendorSpecificConfig

# TODO update the JSON string below
json = "{}"
# create an instance of DVSVendorSpecificConfig from a JSON string
dvs_vendor_specific_config_instance = DVSVendorSpecificConfig.from_json(json)
# print the JSON string representation of the object
print DVSVendorSpecificConfig.to_json()

# convert the object into a dict
dvs_vendor_specific_config_dict = dvs_vendor_specific_config_instance.to_dict()
# create an instance of DVSVendorSpecificConfig from a dict
dvs_vendor_specific_config_form_dict = dvs_vendor_specific_config.from_dict(dvs_vendor_specific_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


