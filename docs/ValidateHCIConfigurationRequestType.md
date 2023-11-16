# ValidateHCIConfigurationRequestType

The parameters of *ClusterComputeResource.ValidateHCIConfiguration*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hci_config_spec** | [**ClusterComputeResourceHCIConfigSpec**](ClusterComputeResourceHCIConfigSpec.md) |  | [optional] 
**hosts** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | The set of hosts to be validated. If not specified, the set of existing hosts in the cluster will be used.   Note:- This param must be omitted for post-configure validation.  Refers instances of *HostSystem*.  | [optional] 

## Example

```python
from vmware_vi.models.validate_hci_configuration_request_type import ValidateHCIConfigurationRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateHCIConfigurationRequestType from a JSON string
validate_hci_configuration_request_type_instance = ValidateHCIConfigurationRequestType.from_json(json)
# print the JSON string representation of the object
print ValidateHCIConfigurationRequestType.to_json()

# convert the object into a dict
validate_hci_configuration_request_type_dict = validate_hci_configuration_request_type_instance.to_dict()
# create an instance of ValidateHCIConfigurationRequestType from a dict
validate_hci_configuration_request_type_form_dict = validate_hci_configuration_request_type.from_dict(validate_hci_configuration_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


