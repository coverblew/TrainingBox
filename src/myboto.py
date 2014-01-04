import boto
print("hace algo");
ec2 = boto.connect_ec2();
print (ec2.get_all_regions());

