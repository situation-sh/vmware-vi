# HostService

Data object that describes a single service that runs on the host. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Brief identifier for the service.  | 
**label** | **str** | Display label for the service.  | 
**required** | **bool** | Flag indicating whether the service is required and cannot be disabled.  | 
**uninstallable** | **bool** | Deprecated this flag is unimplemented and will always be set to false.  Flag indicating whether the service can be uninstalled.  | 
**running** | **bool** | Flag indicating whether the service is currently running.  | 
**ruleset** | **List[str]** | List of firewall rulesets used by this service.  Must come from the list of rulesets in *HostFirewallInfo.ruleset*.  | [optional] 
**policy** | **str** | Service activation policy.  See also *HostServicePolicy_enum*.  | 
**source_package** | [**HostServiceSourcePackage**](HostServiceSourcePackage.md) |  | [optional] 

## Example

```python
from vmware_vi.models.host_service import HostService

# TODO update the JSON string below
json = "{}"
# create an instance of HostService from a JSON string
host_service_instance = HostService.from_json(json)
# print the JSON string representation of the object
print HostService.to_json()

# convert the object into a dict
host_service_dict = host_service_instance.to_dict()
# create an instance of HostService from a dict
host_service_form_dict = host_service.from_dict(host_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


