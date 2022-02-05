Vue.component('select-modal', {
    template:
        `
    <div>
        <b-modal :id="modalName" @shown="focusOK" hide-footer>     
            <div class="d-block text-center">
                <h3>{{ modalMessage }}</h3>
            </div>
            <b-row>
                <b-col></b-col>
                <router-link to="?page=index">
                    <b-button ref="focusThis" variant="danger" @click="isResult=true;select();" id="modal-confirm">はい</b-button>
                </router-link>
                <b-col></b-col>
                <b-button variant="info" @click="isResult=false;select();">いいえ</b-button>
                <b-col></b-col>
            </b-row>
        </b-modal>
    </div>
    `,
    data: {
        isResult: '',
    },
    props: {
        modalName: String,
        modalMessage: String,
    },
    methods: {
        select() {
            this.$emit("selected", isResult);
        },
        focusOK(){
            this.$refs.focusThis.focus();
        }
    }
})