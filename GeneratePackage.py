import os

sfTypeSwitcher = {
    "object": "CustomObject",
    "app": "CustomApplication",
    "appMenu": "AppMenu",
    "approvalProcess": "ApprovalProcess",
    "assignmentRules": "AssignmentRules",
    "autoResponseRules": "AutoResponseRules",
    "cls": "ApexClass",
    "community": "Community",
    "component": "ApexComponent",
    "connectedApp": "ConnectedApp",
    "crt": "Certificate",
    "customPermission": "CustomPermission",
    "duplicateRule": "DuplicateRule",
    "dataSource": "ExternalDataSource",
    "email": "EmailTemplate",
    "escalationRules": "EscalationRules",
    "globalValueSet": "GlobalValueSet",
    "group": "Group",
    "homePageLayout": "HomePageLayout",
    "labels": "CustomLabels",
    "layout": "Layout",
    "letter": "Letterhead",
    "managedTopics": "ManagedTopics",
    "matchingRule": "MatchingRule",
    "network": "Network",
    "object": "CustomObject",
    "objectTranslation": "CustomObjectTranslation",
    "page": "ApexPage",
    "permissionset": "PermissionSet",
    "profile": "Profile",
    "queue": "Queue",
    "quickAction": "QuickAction",
    "remoteSite": "RemoteSiteSettings",
    "reportType": "ReportType",
    "resource": "StaticResource",
    "role": "Role",
    "settings": "Settings",
    "sharingRules": "SharingRules",
    "site": "CustomSite",
    "tab": "CustomTab",
    "translation": "Translations",
    "territory2Type": "Territory2Type",
    "trigger": "ApexTrigger",
    "workflow": "Workflow"
    }

def getType(line):
    linesplit = line.split(".")
    filetype = str(linesplit[-1])
    filetype = filetype.replace("\n","")
    #print(filetype)
    return sfTypeSwitcher.get(filetype,"")

finalFile = open("final.txt","r")
packageFile = open("package.xml","w").close()
packageFile = open("package.xml","a")
#packageFile.write("<?xml version='1.0' encoding='UTF-8'?><Package>")
packageFileContent = "<?xml version='1.0' encoding='UTF-8'?><Package xmlns='http://soap.sforce.com/2006/04/metadata'>"
for line in finalFile:
    sfTypeName = getType(line)
    #print(sfTypeName)
    if (sfTypeName != ""):
        entity = (((line.split("/"))[-1]).split("."))[0]
        print(entity)
        if (packageFileContent.find(sfTypeName + "<") == -1):
            packageFileContent = packageFileContent + "<types><members>" + entity + "</members><name>" + sfTypeName + "</name></types>"
        else:
            location = packageFileContent.find("<name>" + sfTypeName + "</name></types>")
            packageFileContent = packageFileContent[:location] + "<members>" + entity + "</members>" + packageFileContent[location:]
packageFileContent = packageFileContent + "<version>38.0</version></Package>"  
packageFile.write(packageFileContent)
packageFile.close()



    


