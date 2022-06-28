


def gen_master(members):
    codes=[]
    codes.append("<table>")
    codes.append("<tr>")
    for i,member in enumerate(members):
        if i%5==0 and i!=0:
            codes.append("</tr>")
            codes.append("<tr>")

        codes.append(f'<td align="center"><a href="https://github.com/{member[0]}"><img src="https://avatars.githubusercontent.com/u/{member[4]}?v=4?s=120" width="150px;" alt=""/><br /><sub><b>{member[2]}({member[3]})</b></sub></a><br /></td>')
    codes.append("</tr>")
    codes.append("</table>")
    return "\n".join(codes)

def gen_phd(members):
    codes=[]
    codes.append("<table>")
    codes.append("<tr>")
    for i,member in enumerate(members):
        if i%4==0 and i!=0:
            codes.append("</tr>")
            codes.append("<tr>")
        codes.append(f'<td align="center"><a href="https://github.com/{member[0]}"><img src="https://avatars.githubusercontent.com/u/{member[4]}?v=4?s=120" width="150px;" alt=""/><br /><sub><b>{member[2]}({member[3]})</b></sub></a><br /></td>')

    codes.append("</tr>")
    codes.append("</table>")
    return "\n".join(codes)

members = open("csu-eis_members.csv").readlines()

print(members)
phds=[]
masters=[]
mentors=[]

for member in members[1:]:
    items = member.replace('\n','').split(',')
    if items[1] == 'doctor':
        phds.append(items)
    elif items[1] == 'master':
        masters.append(items)
    elif items[1] == 'mentor':
        mentors.append(items)
print(phds)
phds.sort(key=lambda x:int(x[5]))
masters.sort(key=lambda x:int(x[5]))

print(gen_phd(phds))
print()
print(gen_master(masters))