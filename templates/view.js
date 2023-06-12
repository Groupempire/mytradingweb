
      <script>
        //https://docs.google.com/spreadsheets/d/13-yh75noC6nNsWef1hAYYw49l414c6GQ_HY63JIvg8U/edit?usp=sharing
        //gfhghttps://docs.google.com/spreadsheets/d/14WtCTT1yBcvza4lp90-8uBSj4equHRm-FqYoS9D2RmM/edit?usp=sharing
        const sheet_id = "14WtCTT1yBcvza4lp90-8uBSj4equHRm-FqYoS9D2RmM";
        fetch(`https://docs.google.com/spreadsheets/d/${sheet_id}/export?format=tsv`).
          then(response => response.text()).
            then(txt => {
              const sheet = txt.split("\r\n").map(r => r.split('\t'));
              let html = "";
              for (let i = sheet.length-1; i>0; i--) {
                html += `
                <style>p{color:;} 
                h3{display:inline;}
                .box p{
                padding-right:25px;
                     text-align:left; 
                }
        .box  h3{text-align::left;
        /*
hfhgsgfgnhdfgjnfdgdfj hfggdfgdfghfdghdf bfdhjdfdfhdfgdff dfhjfhddfhdfhdhfdgdfdfgjdhfghdfjvbjgf fjgfhgjfgdffhffdddvdf hdfgdfghdfjgdfdfhdf
jfdfvjcnvdfvjdfbvh hello hkdfhgfdghdfdfbddsdfgdfhdfbgfjdbvbd hfdshdsahderfgdfvdcvc  hfdghdfvhkdgddsddfvdfj hdfhdbvdfhvbdv
dbdfbvcvcnbvdvnbcxvhjdfbvbcbfjdffdfgd hgfdhghdsgfdfdhgfhfdj fdkjgdfgfdvdjb bfdsjfdvdjdfvbdvbf gfgfugifugrfgfhgdfjgfnbfvbfvbjfnbfjbnfbfbvkfb ndfjgdfjggdfnvdfnbnfbf gfdhgdfbvfdnvdfbvfjdfv bvfdngvdfjgvdfvdfkjvdfvjdf vdfv ndfkdndkdffdvndfbvnfd
dfkdfnbfxbdcbdf  vdfvdfvnzfvbvb nfv bnbfvndfbvdnbvkdvndfnkj dfkghdfvdfvkdfkvdfkbvvkdfvbdf bdfkgfdkvbdfdfgbdfkbvdfv ngfdkvnfd
fvjbfvjmfvfvdvjdfvdfvdvbdbvjdfgbfdjv

        */
        //margin-left:50%;
        }
        .box span{
             font-size:6px;
             
        }
                </style>
           <div style="color:white;" class="box  border-info card text-bg-light mb-1 ">
                  <h3>${sheet[i][0]}</h3>
                    
    <!-- <small>${sheet[i][0]}</small> 
     -->  <span>( ${sheet[i][2]} )</span>
                   
               <p>${sheet[i][1]}</p>
                </div>
             
                <br>
                
                
                `;
              }
              document.querySelector("div#content").innerHTML = html;
        });
      </script>