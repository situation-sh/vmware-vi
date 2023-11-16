# CustomizationSpec

The Specification data object type contains information required to customize a virtual machine when deploying it or migrating it to a new host. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**options** | [**CustomizationOptions**](CustomizationOptions.md) |  | [optional] 
**identity** | [**CustomizationIdentitySettings**](CustomizationIdentitySettings.md) |  | 
**global_ip_settings** | [**CustomizationGlobalIPSettings**](CustomizationGlobalIPSettings.md) |  | 
**nic_setting_map** | [**List[CustomizationAdapterMapping]**](CustomizationAdapterMapping.md) | IP settings that are specific to a particular virtual network adapter.  The AdapterMapping object maps a network adapter&#39;s MAC address to its Adapter settings object. May be empty if there are no network adapters, else should match number of network adapters in the VM.  | [optional] 
**encryption_key** | **List[int]** | Byte array containing the public key used to encrypt any passwords stored in the specification.  Both the client and the server can use this to determine if stored passwords can be decrypted by the server or if the passwords need to be re-entered and re-encrypted before the specification can be used.  | [optional] 

## Example

```python
from vmware_vi.models.customization_spec import CustomizationSpec

# TODO update the JSON string below
json = "{}"
# create an instance of CustomizationSpec from a JSON string
customization_spec_instance = CustomizationSpec.from_json(json)
# print the JSON string representation of the object
print CustomizationSpec.to_json()

# convert the object into a dict
customization_spec_dict = customization_spec_instance.to_dict()
# create an instance of CustomizationSpec from a dict
customization_spec_form_dict = customization_spec.from_dict(customization_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


