echo -n "Please enter private token: "
read -s PRIVATE_TOKEN
number_of_pages=$(curl -s --head "https://gitlab.xxxx.ca/api/v4/projects?private_token=$PRIVATE_TOKEN" | grep -i x-total-pages | awk '{print $2}' | tr -d '\r\n')
for page in $(seq 1 $number_of_pages); do
    curl -s "https://gitlab.xxxx.ca/api/v4/projects?private_token=$PRIVATE_TOKEN&page=$page"
done