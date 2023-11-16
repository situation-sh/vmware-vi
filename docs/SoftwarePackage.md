# SoftwarePackage

Software Packages provide discrete version and packaging.  This data is reported by CLI:: esxcli software vib get -n ...  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Identifier that uniquely identifies the software package.  ***Since:*** vSphere API 6.5  | 
**version** | **str** | Version string uniquely identifies this package.  ***Since:*** vSphere API 6.5  | 
**type** | **str** | Type of vib installed.  See *SoftwarePackageVibType_enum*.  ***Since:*** vSphere API 6.5  | 
**vendor** | **str** | The corporate entity that created this package.  ***Since:*** vSphere API 6.5  | 
**acceptance_level** | **str** | See also *HostImageAcceptanceLevel_enum*.  ***Since:*** vSphere API 6.5  | 
**summary** | **str** | A brief description of the package contents.  ***Since:*** vSphere API 6.5  | 
**description** | **str** | A full account of the package contents.  ***Since:*** vSphere API 6.5  | 
**reference_url** | **List[str]** | The list of SupportReference objects with in-depth support information.  ***Since:*** vSphere API 6.5  | [optional] 
**creation_date** | **datetime** | The time when the package was installed.  On Autodeploy stateless installs there is no set value.  ***Since:*** vSphere API 6.5  | [optional] 
**depends** | [**List[Relation]**](Relation.md) | A list of VIBs that must be installed at the same time as this VIB.  ***Since:*** vSphere API 6.5  | [optional] 
**conflicts** | [**List[Relation]**](Relation.md) | A list of VIBs that cannot be installed at the same time as this VIB for a given version.  ***Since:*** vSphere API 6.5  | [optional] 
**replaces** | [**List[Relation]**](Relation.md) | A list of SoftwareConstraint objects that identify VIBs that replace this VIB or make it obsolete.  VIBs automatically replace VIBs with the same name but lower versions.  ***Since:*** vSphere API 6.5  | [optional] 
**provides** | **List[str]** | A list of virtual packages or interfaces this VIB provides.  ***Since:*** vSphere API 6.5  | [optional] 
**maintenance_mode_required** | **bool** | True if hosts must be in maintenance mode for installation of this VIB.  ***Since:*** vSphere API 6.5  | [optional] 
**hardware_platforms_required** | **List[str]** | A list of hardware platforms this package is supported on.  ***Since:*** vSphere API 6.5  | [optional] 
**capability** | [**SoftwarePackageCapability**](SoftwarePackageCapability.md) |  | 
**tag** | **List[str]** | A list of string tags for this package defined by the vendor or publisher.  Tags can be used to identify characteristics of a package.  ***Since:*** vSphere API 6.5  | [optional] 
**payload** | **List[str]** | A list of string tags to indicate one or more of what is contained: may be one of bootloader, upgrade, bootisobios, bootisoefi, vgz, tgz, boot or other values.  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.software_package import SoftwarePackage

# TODO update the JSON string below
json = "{}"
# create an instance of SoftwarePackage from a JSON string
software_package_instance = SoftwarePackage.from_json(json)
# print the JSON string representation of the object
print SoftwarePackage.to_json()

# convert the object into a dict
software_package_dict = software_package_instance.to_dict()
# create an instance of SoftwarePackage from a dict
software_package_form_dict = software_package.from_dict(software_package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


